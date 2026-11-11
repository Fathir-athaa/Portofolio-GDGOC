// Slider foto untuk kartu Experience, Organization, dan Project.
// - Jumlah slide mengikuti jumlah foto: 1 foto = diam, 2 foto = geser sampai 2, dst.
// - Bentuk tiap foto diatur dari Django admin (kolom "Tampilan" dan "Fokus potong").
//   Tampilan "Asli" mengikuti bentuk foto: potret tampil tinggi, landscape tampil lebar.
// Butuh escapeHtml() dari utils.js (di-load lebih dulu oleh base.html).

const SLIDER_INTERVAL = 4000; // lama tiap foto tampil (milidetik)

// Pilihan "Tampilan" dari admin -> rasio lebar:tinggi. "auto" (Asli) tidak ada di sini.
const SLIDE_RATIOS = { '16/9': [16, 9], '4/3': [4, 3], '1/1': [1, 1], '3/4': [3, 4], '9/16': [9, 16] };
const SLIDE_FOCUS = ['center', 'top', 'bottom', 'left', 'right'];

// Style untuk foto yang dipotong ke rasio tertentu. Tampilan Asli -> tanpa style tambahan.
function slideImageStyle(item) {
  const ratio = SLIDE_RATIOS[item.display];
  if (!ratio) return '';
  const [w, h] = ratio;
  const focus = SLIDE_FOCUS.includes(item.focus) ? item.focus : 'center';
  return `aspect-ratio: ${w} / ${h}; width: min(100%, calc(var(--slide-max-h) * ${w} / ${h}));`
    + ` object-fit: cover; object-position: ${focus};`;
}

// Membuat HTML slider. images = daftar { url, display, focus } dari API
// (daftar URL biasa juga diterima). Kalau tidak ada foto, hasilnya string kosong.
function buildImageSlider(images, altText) {
  const items = (images || []).map(item => (typeof item === 'string' ? { url: item } : item));
  if (items.length === 0) return '';

  const slides = items.map((item, i) => `
    <div class="exp-slide">
      <img class="exp-slide__img" src="${escapeHtml(item.url)}" style="${slideImageStyle(item)}"
           alt="Foto ${i + 1} ${escapeHtml(altText)}">
    </div>`).join('');

  // titik penanda hanya muncul kalau fotonya lebih dari 1
  const dots = items.length > 1
    ? `<div class="exp-slider-dots">${items.map((_, i) =>
        `<button type="button" class="exp-slider-dot${i === 0 ? ' is-active' : ''}"
                 data-slide="${i}" aria-label="Lihat foto ${i + 1}"></button>`).join('')}</div>`
    : '';

  return `
    <div class="exp-image" data-count="${items.length}" data-index="0">
      <div class="exp-slider-track">${slides}</div>
      ${dots}
    </div>`;
}

// Tinggi bingkai disamakan dengan tinggi foto yang sedang tampil.
function fitSliderHeight(slider) {
  if (!slider) return;
  const slide = slider.querySelectorAll('.exp-slide')[Number(slider.dataset.index)];
  if (slide && slide.offsetHeight > 0) slider.style.height = `${slide.offsetHeight}px`;
}

// Pindah ke foto ke-index (kembali ke foto pertama setelah foto terakhir).
function showSlide(slider, index) {
  const count = Number(slider.dataset.count);
  const next = ((index % count) + count) % count;
  slider.dataset.index = next;
  slider.querySelector('.exp-slider-track').style.transform = `translateX(-${next * 100}%)`;
  slider.querySelectorAll('.exp-slider-dot').forEach((dot, i) => {
    dot.classList.toggle('is-active', i === next);
  });
  fitSliderHeight(slider);
}

// Geser otomatis semua slider di halaman. Berhenti sementara saat kursor di atas foto.
setInterval(() => {
  document.querySelectorAll('.exp-image[data-count]').forEach(slider => {
    if (Number(slider.dataset.count) < 2 || slider.matches(':hover')) return;
    showSlide(slider, Number(slider.dataset.index) + 1);
  });
}, SLIDER_INTERVAL);

// Klik titik penanda untuk langsung ke foto tertentu.
document.addEventListener('click', event => {
  const dot = event.target.closest('.exp-slider-dot');
  if (!dot) return;
  showSlide(dot.closest('.exp-image'), Number(dot.dataset.slide));
});

// Ukuran asli foto baru diketahui setelah foto selesai dimuat, jadi tinggi bingkai dihitung ulang.
document.addEventListener('load', event => {
  if (event.target instanceof HTMLImageElement && event.target.matches('.exp-slide__img')) {
    fitSliderHeight(event.target.closest('.exp-image'));
  }
}, true);

window.addEventListener('resize', () => {
  document.querySelectorAll('.exp-image[data-count]').forEach(fitSliderHeight);
});
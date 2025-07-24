document.addEventListener("DOMContentLoaded", () => {
  tinymce.init({
    selector: '#id_content',  // change this value according to your HTML
    license_key: 'gpl',
    language: 'ru',
    promotion: false,
    onboarding: false,
    branding: false,
    plugins: ['link', 'code', 'wordcount', 'searchreplace', 'preview', 'codesample', 'fullscreen'],
    toolbar: 'undo redo | styles | bold italic | code | link unlink searchreplace | preview codesample fullscreen',
    link_rel_list: [
      { title: 'No Referrer', value: 'noreferrer' },
      { title: 'External Link', value: 'external' }
    ]
  });
});

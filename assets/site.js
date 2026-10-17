(() => {
  const search = document.getElementById('paper-search');
  const year = document.getElementById('paper-year');
  if (search && year) {
    const papers = [...document.querySelectorAll('#paper-list .publication')];
    const status = document.querySelector('.filter-status');
    const update = () => {
      const query = search.value.trim().toLocaleLowerCase();
      let count = 0;
      for (const paper of papers) {
        const visible = (!year.value || paper.dataset.year === year.value) && paper.textContent.toLocaleLowerCase().includes(query);
        paper.hidden = !visible;
        if (visible) count++;
      }
      document.getElementById('no-results').hidden = count !== 0;
      status.textContent = `${count} ${status.dataset.label}`;
    };
    search.addEventListener('input', update);
    year.addEventListener('change', update);
  }
  document.querySelector('.print-button')?.addEventListener('click', () => window.print());
})();

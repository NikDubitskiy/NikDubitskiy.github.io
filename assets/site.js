(() => {
  const ru = document.documentElement.lang === 'ru';
  const toggle = document.querySelector('.theme-toggle');
  const paint = () => {
    const dark = document.documentElement.dataset.theme === 'dark';
    if (toggle) {
      toggle.hidden = false;
      toggle.setAttribute('aria-label', ru ? (dark ? 'Включить дневную тему' : 'Включить ночную тему') : (dark ? 'Switch to light theme' : 'Switch to dark theme'));
      toggle.setAttribute('aria-pressed', String(dark));
      toggle.querySelector('.theme-label').textContent = ru ? (dark ? 'Ночная' : 'Дневная') : (dark ? 'Dark' : 'Light');
    }
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content',dark ? '#141916' : '#f0f0e9');
  };
  paint();
  toggle?.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = theme;
    try { localStorage.setItem('nd-theme',theme); } catch (_) {}
    paint();
  });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    let saved;try { saved=localStorage.getItem('nd-theme'); } catch (_) {}
    if (!saved) {document.documentElement.dataset.theme=e.matches?'dark':'light';paint();}
  });
  const search = document.getElementById('paper-search');
  const year = document.getElementById('paper-year');
  if (search && year) {
    search.closest('form').addEventListener('submit',e=>e.preventDefault());
    const papers = [...document.querySelectorAll('#papers .publication')];
    const status = document.querySelector('.filter-status');
    const update = () => {
      const query = search.value.trim().toLocaleLowerCase();let count=0;
      for (const paper of papers) {
        const visible = (!year.value || paper.dataset.year===year.value) && paper.textContent.toLocaleLowerCase().includes(query);
        paper.hidden=!visible;if(visible)count++;
      }
      document.getElementById('no-results').hidden=count!==0;
      status.textContent=`${status.dataset.label} ${count}`;
    };
    search.addEventListener('input',update);year.addEventListener('change',update);
  }
  document.querySelectorAll('.contact-form').forEach(form=>{
    form.addEventListener('submit',e=>{
      e.preventDefault();
      const subject=form.elements.subject.value.trim();const body=form.elements.body.value.trim();
      if(!subject || !body)return;
      const href=form.action.split('?')[0]+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
      form.querySelector('.mail-status').textContent=ru?'Открываем почтовое приложение. Если оно не появилось, скопируйте адрес и текст письма.':'Opening your email app. If it does not appear, copy the address and message.';
      const draft=document.createElement('a');draft.href=href;draft.target='_blank';draft.rel='noopener';draft.hidden=true;document.body.appendChild(draft);draft.click();draft.remove();
    });
    form.querySelector('.copy-email')?.addEventListener('click',async e=>{
      try {await navigator.clipboard.writeText(e.currentTarget.dataset.email);form.querySelector('.mail-status').textContent=ru?'Адрес скопирован.':'Address copied.';}
      catch(_){form.querySelector('.mail-status').textContent=ru?'Выделите и скопируйте адрес вручную.':'Select and copy the address manually.';}
    });
  });
  const dialog=document.querySelector('.image-dialog');
  if(dialog && typeof dialog.showModal==='function'){
    document.querySelectorAll('[data-lightbox]').forEach(link=>link.addEventListener('click',e=>{
      e.preventDefault();const im=link.querySelector('img');dialog.querySelector('img').src=link.href;dialog.querySelector('img').alt=im.alt;dialog.querySelector('p').textContent=im.alt;dialog.showModal();
    }));
    dialog.querySelector('.close-image').addEventListener('click',()=>dialog.close());
    dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
  }
})();

// Progressive enhancement: every page remains readable without JavaScript.
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if(!reduced.matches) document.body.classList.add('motion-enabled');
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  if (menu && nav) {
    menu.hidden = false;
    document.body.classList.add('menu-enabled');
    const close = () => { menu.setAttribute('aria-expanded','false'); nav.classList.remove('is-open'); };
    menu.addEventListener('click', () => {
      const open = menu.getAttribute('aria-expanded') !== 'true';
      menu.setAttribute('aria-expanded',String(open)); nav.classList.toggle('is-open',open);
    });
    document.addEventListener('keydown',e=>{if(e.key==='Escape' && nav.classList.contains('is-open')){close();menu.focus();}});
    matchMedia('(min-width: 601px)').addEventListener('change',close);
  }
  if ('IntersectionObserver' in window) {
    const reveal = new IntersectionObserver(entries=>entries.forEach(entry=>{
      if(entry.isIntersecting){entry.target.classList.add('is-visible');reveal.unobserve(entry.target);}
    }),{threshold:0.06});
    if(!reduced.matches) document.querySelectorAll('.article-section,.atlas-item,.home-end').forEach(el=>{
      // Only animate content below the initial viewport; no hidden hero or delayed LCP.
      if(el.getBoundingClientRect().top>innerHeight){el.classList.add('reveal-ready');reveal.observe(el);}
    });
    reduced.addEventListener('change',()=>{if(reduced.matches){document.querySelectorAll('.reveal-ready').forEach(el=>el.classList.add('is-visible'));reveal.disconnect();}});
  }
  const bar=document.querySelector('.reading-progress');
  const links=[...document.querySelectorAll('.contents a[href^="#"]')];
  const sections=links.map(a=>document.getElementById(a.hash.slice(1)));
  let pending=false;
  const update=()=>{
    const height=document.documentElement.scrollHeight-innerHeight;
    if(bar)bar.style.transform=`scaleX(${height>0?Math.min(1,Math.max(0,scrollY/height)):0})`;
    let current=-1;sections.forEach((el,i)=>{if(el && el.getBoundingClientRect().top<=240)current=i;});
    links.forEach((a,i)=>{if(i===current)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});pending=false;
  };
  addEventListener('scroll',()=>{if(!pending){pending=true;requestAnimationFrame(update);}},{passive:true});
  addEventListener('resize',update);update();
})();

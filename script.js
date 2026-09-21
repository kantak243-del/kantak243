document.addEventListener('DOMContentLoaded', () => {
  // タブ切替
  document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
    });
  });

  // いいねボタン
  document.querySelectorAll('.action.like').forEach(btn => {
    btn.addEventListener('click', () => {
      const countEl = btn.querySelector('.count');
      const liked = btn.classList.toggle('liked');
      const current = parseInt(countEl.textContent.replace(/,/g, ''), 10) || 0;
      countEl.textContent = (liked ? current + 1 : current - 1).toLocaleString('ja-JP');
    });
  });

  // 保存ボタン
  document.querySelectorAll('.action.bookmark').forEach(btn => {
    btn.addEventListener('click', () => {
      const countEl = btn.querySelector('.count');
      const saved = btn.classList.toggle('liked');
      const current = parseInt(countEl.textContent.replace(/,/g, ''), 10) || 0;
      countEl.textContent = (saved ? current + 1 : current - 1).toLocaleString('ja-JP');
    });
  });

  // コインバッジを閉じる
  document.querySelectorAll('.coin-badge').forEach(badge => {
    badge.addEventListener('click', (e) => {
      if (e.target.classList.contains('coin-close')) {
        badge.style.display = 'none';
      }
    });
  });

  // 下部ナビの選択状態
  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
      item.classList.add('active');
    });
  });
});

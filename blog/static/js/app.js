document.addEventListener('DOMContentLoaded', function() {
    // ローディング画面を非表示にする
    function hideLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        loadingScreen.style.display = 'none';
    }

    // 本文のコンテンツを表示する
    function showContent() {
        const content = document.getElementById('content');
        content.style.opacity = 1;
    }

    // ローディング画面を非表示にしてコンテンツを表示する
    setTimeout(function() {
        window.location.href = '/start';
    }, 5000); // 5秒後に非表示にする例
});



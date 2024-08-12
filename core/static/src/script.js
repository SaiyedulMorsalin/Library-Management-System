const clickTab = (tab) => {
    // Remove 'tab-active' class from all tabs
    document.querySelectorAll('.tab').forEach(element => {
        element.classList.remove('tab-active');
    });

    // Add 'tab-active' class to the clicked tab
    tab.classList.add('tab-active');
}
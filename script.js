document.addEventListener('DOMContentLoaded', () => {
    initChapterCharts();
});

function initChapterCharts() {
    const ctxTalents = document.getElementById('chartTalentsTVL');
    if (ctxTalents) {
        new Chart(ctxTalents, {
            type: 'line',
            data: {
                labels: ['2021', '2022', '2023', '2024', '2025', '2026(Proj)'],
                datasets: [{
                    label: 'Développeurs Actifs (Solana)',
                    data: [2500, 3200, 4100, 5800, 8500, 12000],
                    borderColor: '#14F195',
                    backgroundColor: 'rgba(20, 241, 149, 0.1)',
                    fill: true,
                    tension: 0.4
                }, {
                    label: 'TVL ($B)',
                    data: [1.2, 0.8, 2.5, 4.8, 12.5, 25.0],
                    borderColor: '#9945FF',
                    borderDash: [5, 5],
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { labels: { color: '#cbd5e1', font: { family: 'JetBrains Mono' } } } },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#94a3b8' } },
                    x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
                }
            }
        });
    }

    const ctxJobIndex = document.getElementById('chartJobIndex');
    if (ctxJobIndex) {
        new Chart(ctxJobIndex, {
            type: 'line',
            data: {
                labels: ['2021', '2022', '2023', '2024', '2025', '2026(Proj)'],
                datasets: [{
                    label: 'Index Emploi Web3',
                    data: [100, 140, 120, 190, 280, 380],
                    borderColor: '#14F195',
                    backgroundColor: 'rgba(20, 241, 149, 0.1)',
                    fill: true,
                    tension: 0.4
                }, {
                    label: 'Index Emploi Web2',
                    data: [100, 105, 108, 110, 112, 115],
                    borderColor: '#9945FF',
                    borderDash: [5, 5],
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { labels: { color: '#cbd5e1', font: { family: 'JetBrains Mono' } } } },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#94a3b8' } },
                    x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
                }
            }
        });
    }
}

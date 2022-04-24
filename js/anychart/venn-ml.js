anychart.onDocumentReady(function () {

    anychart.theme('pastel');

    var data = [
        {
            x: 'A',
            value: 100,
            name: '数学',
            tooltipTitle: '矩阵论、最优化',
            tooltipDesc: '数据大多以矩阵形式呈现，模型求解需要最优化技术',
            normal: { fill: "#8ecafb 0.7" },
            hovered: { fill: "#8ecafb 1" },
            selected: { fill: "#8ecafb 1" }
        },
        {
            x: 'B',
            value: 100,
            name: '统计',
            tooltipTitle: '集中不等式、大数定律、随机过程',
            tooltipDesc: '机器学习算法是概率近似正确的，概率有多大，近似有多好',
            normal: { fill: "#ffeaa6 0.7" },
            hovered: { fill: "#ffeaa6 1" },
            selected: { fill: "#ffeaa6 1" }
        },
        {
            x: 'C',
            value: 100,
            name: '计算机',
            tooltipTitle: '算法实现、分布式学习',
            tooltipDesc: '机器学习处理的数据集越来越大，算法的高效实现至关重要',
            normal: { fill: "#ee957f 0.7" },
            hovered: { fill: "#ee957f 1" },
            selected: { fill: "#ee957f 1" }
        },
        {
            x: ['A', 'C'],
            value: 40,
            name: '',
            tooltipTitle: '',
            tooltipDesc: '',
            normal: { fill: "#a98caf 0.6" },
            hovered: { fill: "#a98caf 1" },
            selected: { fill: "#a98caf 1" },
            hatchFill: {
                type: "weave",
                color: "#8b6b92"
            }
        },
        {
            x: ['A', 'B'],
            value: 40,
            name: '',
            tooltipTitle: '',
            tooltipDesc: '',
            normal: { fill: "#9fdebe 0.8" },
            hovered: { fill: "#9fdebe 1" },
            selected: { fill: "#9fdebe 1" },
            hatchFill: {
                type: "weave",
                color: "#83c3a3"
            }
        },
        {
            x: ['B', 'C'],
            value: 40,
            name: '',
            tooltipTitle: '',
            tooltipDesc: '',
            normal: { fill: "#f5b57c 0.8" },
            hovered: { fill: "#f5b57c 1" },
            selected: { fill: "#f5b57c 1" },
            hatchFill: {
                type: "weave",
                color: "#d09259"
            }
        },
        {
            x: ['A', 'B', 'C'],
            value: 70,
            name: '机器学习',
            tooltipTitle: '机器学习',
            tooltipDesc: '来自不同研究领域的人形成了众多的机器学习流派',
            label: { enabled: true, fontStyle: 'normal' },
            normal: { fill: "#8392ab 0.9" },
            hovered: { fill: "#8392ab 1" },
            selected: { fill: "#8392ab 1" },
            hatchFill: {
                type: "percent40",
                color: "#5f6b7d"
            }
        }
    ];

    // create venn diagram
    var chart = anychart.venn(data);

    // set chart title
    chart
        .title()
        .enabled(true)
        .fontFamily('Ysabeau, LXGWWenKai')
        .fontSize(32)
        .padding({ bottom: 0 })
        .text('');

    // set chart stroke
    chart.stroke('1 #fff');

    // set labels settings
    chart
        .labels()
        .fontSize(36)
        .fontColor('#5e6469')
        .hAlign("center")
        .vAlign("center")
        .fontFamily('Ysabeau, LXGWWenKai')
        .fontWeight('700')
        .format('{%Name}');

    // set intersections labels settings
    chart
        .intersections()
        .labels()
        .fontStyle('italic')
        .fontColor('#fff')
        .fontFamily('Ysabeau, LXGWWenKai')
        .format('{%Name}');

    // disable legend
    chart.legend(false);

    // set tooltip settings
    chart
        .tooltip()
        .titleFormat('{%tooltipTitle}')
        .format("{%tooltipDesc}")
        .fontFamily('Ysabeau, LXGWWenKai')
        .background().fill("#000 0.5");

    // set container id for the chart
    chart.container('venn-ml');

    // initiate chart drawing
    chart.draw();
});
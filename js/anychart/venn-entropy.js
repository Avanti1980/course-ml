anychart.onDocumentReady(function () {

    anychart.theme('pastel');

    var data = [
        {
            x: 'A',
            value: 80,
            name: 'H(X|Y)',
            tooltipTitle: '条件熵',
            tooltipDesc: '给定Y后，X还具有的不确定性',
            normal: { fill: "#8ecafb 0.7" },
            hovered: { fill: "#8ecafb 1" },
            selected: { fill: "#8ecafb 1" }
        },
        {
            x: 'B',
            value: 80,
            name: 'H(Y|X)',
            tooltipTitle: '条件熵',
            tooltipDesc: '给定X后，Y还具有的不确定性',
            normal: { fill: "#ffeaa6 0.7" },
            hovered: { fill: "#ffeaa6 1" },
            selected: { fill: "#ffeaa6 1" }
        },
        {
            x: ['A', 'B'],
            value: 40,
            name: 'I(X;Y)',
            tooltipTitle: '互信息',
            tooltipDesc: '给定X后，Y的不确定性的缩减量\n给定Y后，X的不确定性的缩减量',
            normal: { fill: "#9fdebe 0.8" },
            hovered: { fill: "#9fdebe 1" },
            selected: { fill: "#9fdebe 1" },
            hatchFill: {
                type: "weave",
                color: "#83c3a3"
            }
        },
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
        .fontWeight('900')
        .format('{%Name}');

    // set intersections labels settings
    chart
        .intersections()
        .labels()
        .fontColor('#5e6469')
        .fontFamily('Ysabeau, LXGWWenKai')
        .format('{%Name}');

    // disable legend
    chart.legend(false);

    // set tooltip settings
    chart
        .tooltip()
        .titleFormat('{%tooltipTitle}')
        .fontSize(18)
        .fontWeight('900')
        .format("{%tooltipDesc}")
        .fontFamily('Ysabeau, LXGWWenKai')
        .background().fill("#000 0.5");

    // set container id for the chart
    chart.container('venn-entropy');

    // initiate chart drawing
    chart.draw();
});
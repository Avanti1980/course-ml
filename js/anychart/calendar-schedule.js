anychart.onDocumentReady(function () {
    // create data
    var data = [
        { x: "2022-04-27", value: "9" },
        { x: "2022-04-29", value: "9" },
        { x: "2022-01-18", value: "9" },
        { x: "2022-01-19", value: "9" },
        { x: "2022-02-03", value: "9" },
        { x: "2022-02-19", value: "9" },
        { x: "2022-03-19", value: "9" }
    ];

    // create a chart and set the data
    var chart = anychart.calendar(data);

    // configure days
    var days = chart.days();
    days.hovered().fill("#b00707");
    days.normal().stroke("#01579b");
    days.hovered().stroke("#b00707");
    days.noDataFill("#f6efef");
    days.noDataHatchFill(null);
    days.noDataStroke("#f6efef");
    days.spacing(4);

    var weeks = chart.weeks();
    weeks.showWeekends(false);
    weeks.labels().fontColor("#dd2c00");
    weeks.labels().fontWeight(600);
    weeks.labels().fontStyle('italic');
    weeks.rightSpace(10);

    // configure months
    var months = chart.months();
    months.stroke("#0767b1", 2);
    months.noDataStroke("#dd2c00");
    months.labels().fontColor("#dd2c00");
    months.labels().fontWeight(600);
    months.labels().fontStyle('italic');
    months.underSpace(20);

    // configure years
    years = chart.years();
    years.inverted(true);
    years.background("#e7f3fd");
    years.title().fontColor("#dd2c00");
    years.title().fontSize(30);
    years.title().fontWeight(600);
    years.underSpace(4);

    // set the container id
    chart.container("calendar-schedule");

    // initiate drawing the chart
    chart.draw();

});

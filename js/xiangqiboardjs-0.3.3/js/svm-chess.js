(function () {
    function isTouchDevice() {
        return ('ontouchstart' in document.documentElement)
    }

    function init() {
        const board2 = Xiangqiboard('board2', {
            draggable: true,
            dropOffBoard: 'trash',
            sparePieces: true
        })

        $('#startBtn').on('click', board2.start)
        $('#clearBtn').on('click', board2.clear)
    }

    $(document).ready(init)
})()
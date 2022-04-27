var wavesurfer = WaveSurfer.create({
    container: '#waveform'
});
wavesurfer.load('../audio/a.m4a');
// 播放和暂停
btnPlay.addEventListener('click', function () {
    wavesurfer.play();
});
btnPause.addEventListener('click', function () {
    wavesurfer.pause();
});
var wavesurfer = WaveSurfer.create({
    container: '#waveform'
});
wavesurfer.load('../audio/Titanic.wav');
// 播放和暂停
btnPlay.addEventListener('click', function () {
    wavesurfer.play();
});
btnPause.addEventListener('click', function () {
    wavesurfer.pause();
});
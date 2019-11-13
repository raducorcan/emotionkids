function handleDataAvailableVideo(event) {
    console.log("data-available");
    if (event.data.size > 0) {
        recordedChunksVideo.push(event.data);
        console.log(recordedChunksVideo);
        download(recordedChunksVideo, "video/webm", "test_video.webm")
    }
}

function handleDataAvailableAudio(event) {
    console.log("data-available");
    if (event.data.size > 0) {
        recordedChunksAudio.push(event.data);
        console.log(recordedChunksAudio);
        download(recordedChunksAudio, "audio/webm", "test_audio.webm")

    }
}

function download(parts, blobType, fileName) {
    let blob = new Blob(parts, {
        type: blobType
    });
    let url = URL.createObjectURL(blob);
    let a = document.createElement("a");
    document.body.appendChild(a);
    a.style = "display: none";
    a.href = url;
    a.download = fileName;
    a.click();
    window.URL.revokeObjectURL(url);
}

function unload() {
    console.log("stopping");
    mediaRecorderVideo.stop();
    mediaRecorderAudio.stop();
    return null;
}
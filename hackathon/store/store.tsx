import { makeAutoObservable } from "mobx";

class VideoStore {
    videoFile: File | null = null;
    viewCount = 0;
    suspectedWords: string[] | null = null;
    fullText: string | null = null;

    constructor() {
        makeAutoObservable(this);
    }

    setVideoFile(file: File) {
        this.videoFile = file;
    }

    incrementViewCount() {
        this.viewCount++;
    }
}

const videoStore = new VideoStore();
export default videoStore;

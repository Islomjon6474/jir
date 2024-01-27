import VideoInput from "@/components/VideoInput";
import VideoViewer from "@/components/VideoWiever";
import VideoTextAnalyser from "@/components/VideoTextAnalyser";


export default function Home() {
  return (
    <main
      className={`flex min-h-screen h-screen flex-col items-center justify-between p-24 mx-10 text-black`}
    >
      <VideoInput />
      <VideoViewer videoSrc="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" />
      <VideoTextAnalyser fullText={"Lorem ipsum fjsfkjsdlfj fsdljfsoafjsodfj"} suspectedWords={['Lorem', 'ipsum', 'fjsfkjsdlfj']} />
    </main>
  );
}

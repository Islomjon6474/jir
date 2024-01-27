import React from 'react';
import VideoInput from "@/components/VideoInput";
import VideoViewer from "@/components/VideoViewer"; // Corrected typo in the import
import VideoTextAnalyser from "@/components/VideoTextAnalyser";
import { observer } from 'mobx-react';
import videoStore from '@/store/store';

const Home = observer(() => {
  return (
      <main className="flex min-h-screen h-screen flex-col items-center justify-between p-24 mx-10 text-black">
        <VideoInput />
        <VideoViewer videoSrc={"https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"} />
        <VideoTextAnalyser
            fullText={videoStore.fullText || "Lorem ipsum fjsfkjsdlfj fsdljfsoafjsodfj"}
            suspectedWords={videoStore.suspectedWords || ['Lorem', 'ipsum', 'fjsfkjsdlfj']}
        />
      </main>
  );
});

export default Home;

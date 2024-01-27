import VideoInput from "@/components/VideoInput";


export default function Home() {
  return (
    <main
      className={`flex min-h-screen h-screen flex-col items-center justify-between p-24 mx-10 text-black`}
    >
      <VideoInput />
    </main>
  );
}

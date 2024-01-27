import React from 'react';

type Props = {
    videoSrc: string;
};

const VideoViewer: React.FC<Props> = ({ videoSrc }) => {
    return (
        <div className="w-full h-auto bg-black">
            <video
                src={videoSrc}
                controls
                className="w-full h-auto"
            >
                Your browser does not support the video tag.
            </video>
        </div>
    );
}

export default VideoViewer;

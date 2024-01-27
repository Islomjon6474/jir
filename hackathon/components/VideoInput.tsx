import React, { useState } from 'react';

type Props = {};

const VideoInput: React.FC<Props> = () => {
    const [videoFile, setVideoFile] = useState<File | null>(null);
    const [dragging, setDragging] = useState(false);

    const handleDragEnter = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        e.stopPropagation();
        setDragging(true);
    };

    const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        e.stopPropagation();
        setDragging(false);
    };

    const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        e.stopPropagation();
    };

    const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        e.stopPropagation();
        setDragging(false);
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            setVideoFile(e.dataTransfer.files[0]);
        }
    };

    const handleVideoChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files ? event.target.files[0] : null;
        setVideoFile(file);
    };

    return (
        <div
            className={`w-full h-1/2 rounded border-2 ${dragging ? 'border-blue-500' : 'border-gray-400'} border-dashed p-4 flex flex-col items-center justify-evenly relative`}
            onDragEnter={handleDragEnter}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
        >
            <p className={`text-gray-400 text-2xl`}>Select, or drag and drop the file.</p>

            <input
                id="video-upload"
                type="file"
                accept="video/*"
                onChange={handleVideoChange}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            />
            <div className={`w-[8rem]  h-[8rem] p-8 flex justify-center items-center rounded-full bg-gray-400`}>
                <label htmlFor="video-upload" className="cursor-pointer">
                    <div className="flex flex-col items-center justify-center">
                        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <g id="upload">
                                <path id="Vector" d="M8.38091 25.3333C5.225 25.3333 2.66663 22.8051 2.66663 19.6863C2.66663 16.5675 5.225 14.0392 8.38091 14.0392C8.75974 14.0392 9.12996 14.0756 9.48817 14.1452M19.1746 10.7029C19.9689 10.4255 20.8237 10.2745 21.7142 10.2745C22.5871 10.2745 23.4257 10.4196 24.2067 10.6866M9.48817 14.1452C9.18271 13.3304 9.01583 12.4492 9.01583 11.5294C9.01583 7.37103 12.427 4 16.6349 4C20.5545 4 23.7828 6.92495 24.2067 10.6866M9.48817 14.1452C10.2407 14.2912 10.9403 14.5832 11.5555 14.9901M24.2067 10.6866C27.1906 11.707 29.3333 14.5082 29.3333 17.8039C29.3333 21.4133 26.7634 24.4294 23.3333 25.163" stroke="white" stroke-width="2" stroke-linecap="round"/>
                                <path id="Vector_2" d="M16 21.3335V29.3335M16 21.3335L18.6667 24.0002M16 21.3335L13.3334 24.0002" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                            </g>
                        </svg>
                    </div>
                </label>
            </div>
            {videoFile && <p className="mt-2 text-sm">{videoFile.name}</p>}
        </div>
    );
}

export default VideoInput;

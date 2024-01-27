import React from 'react';

type Props = {
    fullText: string;
    suspectedWords: string[];
};

const VideoTextAnalyzer: React.FC<Props> = ({ fullText, suspectedWords }) => {
    // Function to highlight suspected words in the text
    const highlightText = (text: string, words: string[]) => {
        const regex = new RegExp(`(${words.join('|')})`, 'gi');
        return text.replace(regex, (match) => `<mark class="bg-yellow-200">${match}</mark>`);
    };

    // Create the highlighted text
    const highlightedText = highlightText(fullText, suspectedWords);

    return (
        <div className="space-y-4">
            <div className="p-4 border rounded shadow">
                <h2 className="text-lg font-semibold mb-2">Full Text</h2>
                <p dangerouslySetInnerHTML={{ __html: highlightedText }}></p>
            </div>
            <div className="p-4 border rounded shadow">
                <h2 className="text-lg font-semibold mb-2">Suspected Words</h2>
                <ul>
                    {suspectedWords.map((word, index) => (
                        <li key={index} className="text-red-500">{word}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default VideoTextAnalyzer;

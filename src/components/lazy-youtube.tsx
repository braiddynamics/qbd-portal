import React, { useState } from 'react';

interface LazyYouTubeProps {
  videoId: string;
  title: string;
}

export default function LazyYouTube({ videoId, title }: LazyYouTubeProps) {
  const [showVideo, setShowVideo] = useState(false);

  // Automatically fetches the maximum resolution thumbnail from YouTube
  const thumbnailUrl = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;

  return (
    <div 
      style={{ 
        position: 'relative', 
        paddingBottom: '56.25%', 
        height: 0, 
        overflow: 'hidden', 
        borderRadius: '12px', 
        boxShadow: '0 12px 28px rgba(0,0,0,0.15)', 
        backgroundColor: '#000', 
        cursor: 'pointer'
      }} 
      onClick={() => setShowVideo(true)}
    >
      {!showVideo ? (
        <>
          <img 
            src={thumbnailUrl} 
            alt={`Thumbnail for ${title}`} 
            style={{ 
              position: 'absolute', 
              top: 0, 
              left: 0, 
              width: '100%', 
              height: '100%', 
              objectFit: 'cover' 
            }} 
          />
          {/* YouTube-style Play Button */}
          <div 
            style={{ 
              position: 'absolute', 
              top: '50%', 
              left: '50%', 
              transform: 'translate(-50%, -50%)', 
              width: '68px', 
              height: '48px', 
              backgroundColor: 'rgba(255, 0, 0, 0.8)', 
              borderRadius: '12px', 
              display: 'flex', 
              justifyContent: 'center', 
              alignItems: 'center',
              transition: 'background-color 0.2s ease'
            }}
            onMouseOver={(e) => e.currentTarget.style.backgroundColor = 'rgba(255, 0, 0, 1)'}
            onMouseOut={(e) => e.currentTarget.style.backgroundColor = 'rgba(255, 0, 0, 0.8)'}
          >
            <div 
              style={{ 
                width: 0, 
                height: 0, 
                borderTop: '10px solid transparent', 
                borderBottom: '10px solid transparent', 
                borderLeft: '16px solid white', 
                marginLeft: '4px' 
              }}
            ></div>
          </div>
        </>
      ) : (
        <iframe 
          style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }}
          src={`https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0&vq=hd1080`} 
          title={title} 
          frameBorder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowFullScreen
        ></iframe>
      )}
    </div>
  );
}
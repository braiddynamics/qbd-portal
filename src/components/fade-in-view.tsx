import React, { useEffect, useRef, useState, ReactNode } from 'react';

interface FadeInViewProps {
  children: ReactNode;
}

export default function FadeInView({ children }: FadeInViewProps) {
  const [isVisible, setIsVisible] = useState(false);
  const domRef = useRef<HTMLDivElement>(null); 

  useEffect(() => {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          if (domRef.current) observer.unobserve(domRef.current);
        }
      });
    }, { threshold: 0.15 }); 
    
    const current = domRef.current;
    if (current) observer.observe(current);
    return () => { if (current) observer.unobserve(current); };
  }, []);

  return (
    <div ref={domRef} className={`timeline-fade-in ${isVisible ? 'is-visible' : ''}`}>
      {children}
    </div>
  );
}
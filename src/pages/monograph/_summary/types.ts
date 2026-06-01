export interface LightboxImageInfo {
  src: string;
  alt: string;
  description: string;
  math?: string;
}

export interface ChapterBreakdown {
  title: string;
  content: string;
}

export interface SpecialistFocus {
  area: string;
  text: string;
}

export interface DefinitionData {
  term: string;
  definition: string;
}

export interface HistoricalCalloutData {
  title: string;
  text: string;
}

export interface ChapterData {
  num: number;
  part: string;
  title: string;
  taxonomy: string;
  status: string;
  leanProofs: number;
  pythonSims: number;
  executiveEvaluation: string;
  breakdowns: ChapterBreakdown[];
  specialists: SpecialistFocus[];
  analogy: string;
  link: string;
  style: 'A' | 'B' | 'C' | 'D' | 'E';
  definitions: DefinitionData[];
  historicalCallout: HistoricalCalloutData;
  image?: LightboxImageInfo;
  sandbox?: 'lightcone' | 'braid' | 'curvature' | 'timeline' | 'selection';
}

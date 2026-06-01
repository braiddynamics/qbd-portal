import { part1Chapters } from './data/chapters/part-1';
import { part2Chapters } from './data/chapters/part-2';
import { part3Chapters } from './data/chapters/part-3';
import { part4Chapters } from './data/chapters/part-4';
import { part5Chapters } from './data/chapters/part-5';

export const chapters = [
  ...part1Chapters,
  ...part2Chapters,
  ...part3Chapters,
  ...part4Chapters,
  ...part5Chapters
];

export { timelineEvents, partsList } from './data/previews';
export type { ChapterData } from './types';

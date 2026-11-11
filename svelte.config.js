import adapter from '@sveltejs/adapter-static';
import { mdsvex } from 'mdsvex';
import rehypeSlug from 'rehype-slug';
export default {
  extensions: ['.svelte', '.md'],
  preprocess: [mdsvex({ extensions: ['.md'], rehypePlugins: [rehypeSlug] })],
  kit: { adapter: adapter(), paths: { base: '/fedramp-conmon-history' } }
};

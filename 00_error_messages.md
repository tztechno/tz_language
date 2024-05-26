###
# error messages 
###

---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
```
---
```
Import trace for requested module:
./app/page.js
 GET / 500 in 3752ms
 ⨯ ./app/page.js
Error: 
  × You're importing a component that needs useState. It only works in a Client Component but none of its parents are marked with "use client", so they're Server Components by default.
  │ Learn more: https://nextjs.org/docs/getting-started/react-essentials
  │ 
  │ 
   ╭─[/Users/shun_ishii/DockerProjects/pj/my-next/app/page.js:1:1]
 1 │ 
 2 │ import { useState } from 'react';
   ·          ────────
 3 │ 
 4 │ export default function Home() {
 5 │     const [z, setZ] = useState(1000);
   ╰────

Import trace for requested module:
./app/page.js
 GET /_next/static/webpack/db60c50299c2875b.webpack.hot-update.json 500 in 784ms
 ⚠ Fast Refresh had to perform a full reload. Read more: https://nextjs.org/docs/messages/fast-refresh-reload
 GET / 500 in 22ms
```
---

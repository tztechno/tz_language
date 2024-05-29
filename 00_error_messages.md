
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
```
---
```
```
---
```
```
---
```
fatal.nim(54)            sysFatal
Error: unhandled exception: index 1 not in 0 .. 0 [IndexDefect]
```
---
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[8], line 3
      1 y_pred = automl.predict(X_test)
      2 accuracy = sum(y_pred == y_test) / len(y_test)
----> 3 print(f"Accuracy: {accuracy:.4f}")

TypeError: unsupported format string passed to numpy.ndarray.__format__
```
---
```
The operation couldn’t be completed. Unable to locate a Java Runtime that supports apt.
Please visit http://www.java.com for information on installing Java.
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

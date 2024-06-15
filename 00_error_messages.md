
###
# error messages 
###

### latest

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
/judge/Main.zig:43:5: error: use of undeclared identifier 'ans'
    ans="YES";
    ^~~
error: a.out...
error: The following command exited with error code 1:
/opt/zig-linux-x86_64-0.10.1/zig build-exe /judge/Main.zig -OReleaseFast --cache-dir /judge/zig-cache --global-cache-dir /home/runner/.cache/zig --name a.out --pkg-begin string /judge/.gyro/zig-string-JakubSzark-github.com-e842e89f/pkg/zig-string.zig --pkg-end --pkg-begin ziter /judge/.gyro/ziter-Hejsil-github.com-a8aad124/pkg/ziter.zig --pkg-end --enable-cache 
error: the following build command failed with exit code 1:
/judge/zig-cache/o/5297450095ee08f631a822f783f9b1b0/build /opt/zig-linux-x86_64-0.10.1/zig /judge /judge/zig-cache /home/runner/.cache/zig
```
---
```
/judge/Main.zig:43:15: error: no field or member function named 'print' in 'fs.file.File'
    try stdout.print("{s}\n", "YES");
        ~~~~~~^~~~~~
/opt/zig-linux-x86_64-0.10.1/lib/std/fs/file.zig:13:18: note: struct declared here
pub const File = struct {
                 ^~~~~~
referenced by:
    callMain: /opt/zig-linux-x86_64-0.10.1/lib/std/start.zig:614:32
    initEventLoopAndCallMain: /opt/zig-linux-x86_64-0.10.1/lib/std/start.zig:548:51
    remaining reference traces hidden; use '-freference-trace' to see all reference traces

error: a.out...
error: The following command exited with error code 1:
/opt/zig-linux-x86_64-0.10.1/zig build-exe /judge/Main.zig -OReleaseFast --cache-dir /judge/zig-cache --global-cache-dir /home/runner/.cache/zig --name a.out --pkg-begin string /judge/.gyro/zig-string-JakubSzark-github.com-e842e89f/pkg/zig-string.zig --pkg-end --pkg-begin ziter /judge/.gyro/ziter-Hejsil-github.com-a8aad124/pkg/ziter.zig --pkg-end --enable-cache 
error: the following build command failed with exit code 1:
/judge/zig-cache/o/5297450095ee08f631a822f783f9b1b0/build /opt/zig-linux-x86_64-0.10.1/zig /judge /judge/zig-cache /home/runner/.cache/zig

```
---
```
/judge/Main.zig:43:24: error: member function expected 2 argument(s), found 1
    try stdout.writer().print("YES");    
        ~~~~~~~~~~~~~~~^~~~~~
/opt/zig-linux-x86_64-0.10.1/lib/std/io/writer.zig:27:13: note: function declared here
        pub fn print(self: Self, comptime format: []const u8, args: anytype) Error!void {
        ~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
referenced by:
    callMain: /opt/zig-linux-x86_64-0.10.1/lib/std/start.zig:614:32
    initEventLoopAndCallMain: /opt/zig-linux-x86_64-0.10.1/lib/std/start.zig:548:51
    remaining reference traces hidden; use '-freference-trace' to see all reference traces

error: a.out...
error: The following command exited with error code 1:
/opt/zig-linux-x86_64-0.10.1/zig build-exe /judge/Main.zig -OReleaseFast --cache-dir /judge/zig-cache --global-cache-dir /home/runner/.cache/zig --name a.out --pkg-begin string /judge/.gyro/zig-string-JakubSzark-github.com-e842e89f/pkg/zig-string.zig --pkg-end --pkg-begin ziter /judge/.gyro/ziter-Hejsil-github.com-a8aad124/pkg/ziter.zig --pkg-end --enable-cache 
error: the following build command failed with exit code 1:
/judge/zig-cache/o/5297450095ee08f631a822f783f9b1b0/build /opt/zig-linux-x86_64-0.10.1/zig /judge /judge/zig-cache /home/runner/.cache/zig
```
---
```
Main.kt:8:11: error: expecting an element
    int Y = Integer.parseInt(X);
          ^
Main.kt:8:20: error: expecting an element
    int Y = Integer.parseInt(X);
                   ^
Main.kt:4:18: error: not nullable value required to call an 'iterator()' method on for-loop range
    for (char in X) {
                 ^
Main.kt:5:31: error: overload resolution ambiguity: 
public open fun getNumericValue(p0: Char): Int defined in java.lang.Character
public open fun getNumericValue(p0: Int): Int defined in java.lang.Character
        val digit = Character.getNumericValue(char)
                              ^
Main.kt:6:11: error: overload resolution ambiguity: 
public final operator fun plus(other: Byte): Int defined in kotlin.Int
public final operator fun plus(other: Double): Double defined in kotlin.Int
public final operator fun plus(other: Float): Float defined in kotlin.Int
public final operator fun plus(other: Int): Int defined in kotlin.Int
public final operator fun plus(other: Long): Long defined in kotlin.Int
public final operator fun plus(other: Short): Int defined in kotlin.Int
        M += digit
          ^
Main.kt:8:5: error: unresolved reference: int
    int Y = Integer.parseInt(X);
    ^
Main.kt:9:9: error: unresolved reference: Y
    if (Y%M==0){
        ^
```
---
```
Main.java:12: error: no suitable method found for getNumericValue(String)
        int Y=Character.getNumericValue(X);
                       ^
    method Character.getNumericValue(char) is not applicable
      (argument mismatch; String cannot be converted to char)
    method Character.getNumericValue(int) is not applicable
      (argument mismatch; String cannot be converted to int)
1 error
```
---
```
Main.java:5: error: cannot find symbol
        String X = sc.next();
                   ^
  symbol:   variable sc
  location: class Main
Main.java:12: error: no suitable method found for getNumericValue(String)
        int Y=Character.getNumericValue(X);
                       ^
    method Character.getNumericValue(char) is not applicable
      (argument mismatch; String cannot be converted to char)
    method Character.getNumericValue(int) is not applicable
      (argument mismatch; String cannot be converted to int)
2 errors

```
---
```
127.0.0.1/:1 Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
```
---
```
# atcoder.jp/golang
./main.go:13:9: err declared and not used
./main.go:13:29: cannot use r (variable of type rune) as string value in argument to strconv.Atoi
```
---
```
RuntimeError: shape '[-1, 46656]' is invalid for input of size 184512
```
---
```
% cargo run
   Compiling my_proj v0.1.0 (/Users/shun_ishii/DockerProjects/pj2/my_proj)
error[E0432]: unresolved import `rocket::response::content::Html`
 --> src/main.rs:7:5
  |
7 | use rocket::response::content::Html;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no `Html` in `response::content`

error[E0599]: no method named `ok` found for opaque type `impl std::future::Future<Output = Result<NamedFile, std::io::Error>>` in the current scope
  --> src/main.rs:19:54
   |
19 |     NamedFile::open(Path::new("static/").join(file)).ok()
   |                                                      ^^ method not found in `impl Future<Output = Result<NamedFile, Error>>`
   |
help: consider `await`ing on the `Future` and calling the method on its `Output`
   |
19 |     NamedFile::open(Path::new("static/").join(file)).await.ok()
   |                                                      ++++++

Some errors have detailed explanations: E0432, E0599.
For more information about an error, try `rustc --explain E0432`.
error: could not compile `my_proj` (bin "my_proj") due to 2 previous errors
```
---



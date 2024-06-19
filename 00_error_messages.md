
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
go get github.com/revel/revel
go get github.com/revel/cmd/revel
go: go.mod file not found in current directory or any parent directory.
        'go get' is no longer supported outside a module.
        To build and install a command, use 'go install' with a version,
        like 'go install example.com/cmd@latest'
        For more information, see https://golang.org/doc/go-get-install-deprecation
        or run 'go help get' or 'go help install'.
go: go.mod file not found in current directory or any parent directory.
        'go get' is no longer supported outside a module.
        To build and install a command, use 'go install' with a version,
        like 'go install example.com/cmd@latest'
        For more information, see https://golang.org/doc/go-get-install-deprecation
        or run 'go help get' or 'go help install'.
```
---
```
compile: Main.kk
Main.kk(10, 9): error: invalid syntax
 unexpected malformed identifier: a dash must be preceded by a letter or digit, and followed by a letter
 expecting expression or ")"
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



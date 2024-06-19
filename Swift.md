###
# Swift
###

---

Swift言語を使用してシンプルなHTTPサーバーを作成し、"Hello, World!"を返す方法について説明します。

まず、Swiftのバージョンが4以降であることを確認してください。以下の手順でHTTPサーバーを作成します。

1. **プロジェクトの作成**

新しいディレクトリを作成し、その中にプロジェクトを初期化します。

```bash
mkdir HelloServer
cd HelloServer
swift package init --type executable
```

2. **依存関係の追加**

HTTP通信を簡単に扱うために、`swift-nio`パッケージを使用します。`Package.swift`ファイルを開き、`dependencies`セクションに以下の内容を追加します。

```swift
.package(url: "https://github.com/apple/swift-nio.git", from: "2.0.0")
```

3. **コードの追加**

`main.swift`ファイルにHTTPサーバーのコードを記述します。

```swift
import Foundation
import NIO
import NIOHTTP1

let group = MultiThreadedEventLoopGroup(numberOfThreads: System.coreCount)
let bootstrap = ServerBootstrap(group: group)
    .serverChannelOption(ChannelOptions.backlog, value: 256)
    .serverChannelOption(ChannelOptions.socket(SocketOptionLevel(SOL_SOCKET), SO_REUSEADDR), value: 1)
    .childChannelInitializer { channel in
        channel.pipeline.addHandler(HTTPServerPipelineHandler())
    }
    .childChannelOption(ChannelOptions.socket(IPPROTO_TCP, TCP_NODELAY), value: 1)
    .childChannelOption(ChannelOptions.socket(SocketOptionLevel(SOL_SOCKET), SO_REUSEADDR), value: 1)

defer {
    try! group.syncShutdownGracefully()
}

do {
    let serverChannel = try bootstrap.bind(host: "::1", port: 8888).wait()
    print("Server running on:", serverChannel.localAddress!)
    try serverChannel.closeFuture.wait()
} catch {
    print("Error starting server:", error)
}

class HTTPServerPipelineHandler: ChannelInboundHandler {
    typealias InboundIn = HTTPServerRequestPart
    typealias OutboundOut = HTTPServerResponsePart
    
    func channelRead(context: ChannelHandlerContext, data: NIOAny) {
        let reqPart = unwrapInboundIn(data)
        
        switch reqPart {
        case .head(let head):
            let body = "Hello, World!"
            var buffer = context.channel.allocator.buffer(capacity: body.utf8.count)
            buffer.writeString(body)
            
            var headers = HTTPHeaders()
            headers.add(name: "Content-Length", value: "\(buffer.readableBytes)")
            headers.add(name: "Content-Type", value: "text/plain; charset=utf-8")
            
            let responseHead = HTTPResponseHead(version: head.version, status: .ok, headers: headers)
            context.write(self.wrapOutboundOut(.head(responseHead)), promise: nil)
            context.write(self.wrapOutboundOut(.body(.byteBuffer(buffer))), promise: nil)
            context.writeAndFlush(self.wrapOutboundOut(.end(nil)), promise: nil)
        case .body, .end:
            break // We are not handling request body in this example
        }
    }
}
```

4. **ビルドと実行**

コードをビルドし、サーバーを起動します。

```bash
swift build
.build/debug/HelloServer
```

これで、サーバーがポート8888で実行され、ブラウザやcurlコマンドで`http://localhost:8888`にアクセスすると、"Hello, World!"が表示されるはずです。

このコードは非常に基本的なHTTPサーバーですが、Swift NIOを使用することで、より高度な処理や非同期処理を実装することも可能です。

---

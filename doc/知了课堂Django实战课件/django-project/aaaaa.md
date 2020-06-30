```js
var gulp = require("gulp")
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")

// 定义一个处理css文件改动的任务
gulp.task("css",function () {
	gulp.src("./css/*.css")
	.pipe(cssnano())
	.pipe(rename({"suffix":".min"}))
	.pipe(gulp.dest("./css/dist/"))
	.pipe(connect.reload())
});

// 定义一个监听的任务
gulp.task("watch",function () {
	// 监听所有的css文件，然后执行css这个任务
	gulp.watch("./css/*.css",['css'])
});
```
以后只要在终端执行`gulp watch`命令即可自动监听所有的`css`文件，然后自动执行`css`的任务，完成相应的工作。

### 11. 更改文件后，自动刷新浏览器：
以上我们实现了更改一些`css`文件后，可以自动执行处理`css`的任务。但是我们还是需要手动的去刷新浏览器，才能看到修改后的效果。有什么办法能在修改完代码后，自动的刷新浏览器呢。答案是使用`gulp-connect`。`gulp-connect`安装的命令如下：
```shell
npm install gulp-connect --save-dev
```
`gulp-connect`使用的示例代码如下：
```js
var gulp = require("gulp")
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")
var connect = require("gulp-connect")

gulp.task("connect",function () {
	connect.server({
		port: 3000,
		root: './',
		livereload: true
	});
});

// 定义一个处理css文件改动的任务
gulp.task("css",function () {
	gulp.src("./css/*.css")
	.pipe(cssnano())
	.pipe(rename({"suffix":".min"}))
	.pipe(gulp.dest("./css/dist/"))
	.pipe(connect.reload())
});

// 定义一个监听的任务
gulp.task("watch",function () {
	gulp.watch("./css/*.css",['css'])
});

// 执行gulp server开启服务器
gulp.task("server",['connect','watch'])
```
以上我们创建了一个`connect`的任务，这个任务会开启一个`3000`端口，以后我们在访问`html`页面的时候，就需要通过`http://127.0.0.1:3000`的方式来访问了。然后接下来我们还定义了一个`server`任务。这个任务会去执行`connect`和`watch`任务，只要修改了`css`文件，那么就会执行`css`的任务，然后就会自动刷新浏览器。

####   关注上传接口，改任意文件的后缀改成png，如果能上传，就能用。否则直接pass 。网站不能判断文件头，只需改后缀名就能上传图片。如果能用，下载下来验证MD5是否一致
####  任意文件，文件头改png、还原
FFmpeg切成ts 自动生成m3u8
只需要一个命令
### ffmpeg -i ' + file_path + ' -c copy -map 0 -f segment -segment_list index.m3u8 -segment_time 1 output%03d.ts
### 把文件上传cdn。替换 m3u8里面的地址



---
kode : IF5200
tanggal : 2023-02-25 23:16
modified_date : Saturday 25th February 2023 23:16:28
---

# IF5200 - Research
Default Camera Resolution = 340 x 240
# Raspberry Pi 2B
- 900 Mhz Quad core ARM 32 bit Cortex-A7
- 1 GB RAM
| Model     | Camera Resolution | Window Size | FPS       | CPU usage | Memory Usage |                       |
| --------- | ----------------- | ----------- | --------- | --------- | ------------ | --------------------- |
| No model  | Default           | 200         | 76.15     | 42 %      | 345 MB       |                       |
| No Model  | Default           | No Window   | 114362.25 | 9 %       | 344 MB       |                       |
| No Model  | Default           | 500         | 37.6      | 89 %      | 345 MB       |                       |
| No Model  | Default           | 300         | 47.35     | 57 %      | 346 MB       |                       |
| No Model  | Default           | 400         | 55.27     | 86 %      | 345 MB       |                       |
| No Model  | Default           | 1000        | 13.6      | 88 %      | 351 MB       |                       |
| No Model  | Default           | 800         | 19.53     | 88 %      | 348 MB       |                       |
| No Model  | Default           | 1200        | 10.16     | 88 %      | 353 MB       |                       |
| FrontFace | *Default*         | 200         | *28.99*   | 72 %      | 249 MB       |                       |
| FrontFace | 208x208           | 200         | 22.91     | 72 %      | 248 MB       |                       |
| FrontFace | 128x128           | 200         | 24.37     | 72 %      | 249 MB       |                       |
| FrontFace | 64x64             | 200         | 27.7      | 73        | 247 MB       | Face Read but stutter |
| FrontFace | 32x32             | 200         | 30.75     | 72        | 247          | Face Read but blur    |
| FrontFace | 192x128           | 200         | 34.49     | 75 %      | 247 MB       |                       |
| FrontFace | 96x64             | 200         | 40.11     | -         | -            |                       |
|           |                   |             |           |           |              |                       |
## ScreenShot

32x32
![[Pasted image 20230226223643.png]]
![[Pasted image 20230226224807.png]]
192x128
![[Pasted image 20230226223906.png]]
![[Pasted image 20230226224834.png]]

128x128
![[Pasted image 20230226224946.png]]
![[Pasted image 20230226225019.png]]

64x64
![[Pasted image 20230226225140.png]]
![[Pasted image 20230226225204.png]]

# Raspberry Pi 3 B
- 1200 Mhz Quad Core ARMv8 64 bit cortex-A53
- 1 GB RAM
- VideoCore IV 3D GPU

| Model     | Camera Res | FPS       | CPU Usage | Memory Usage | Window size |
| --------- | ---------- | --------- | --------- | ------------ | ----------- |
| FrontFace | 128x128    | 36.43     | 74        | 244 MB       | 200         |
|           | 352x240    | 36.59     | 72        | 244 MB       |             |
|           | 208x208    | 28.63     | 70        | 246 MB       |             |
|           | 64x64      | 40.98     | 72        | 245 MB       |             |
|           | 32x32      | 47.21     | 70        | 246 MB       |             |
|           | 192x128    | 55.53     | 74        | 246 MB       |             |
|           | 96x64      | 62.56     | 76        | 246 MB       |             |
| No Model  | Default    | 177747.96 | 29 %      | 243 MB       | None        |
|           |            |           |           |              |             |

Model with no window

### With Send Request
| Model      | Camera Res | FPS   | Window |
| ---------- | ---------- | ----- | ------ |
| Front Face | 192x128    | 14.41 | 200    |
|            | 192x128    | 54.55 | None   |
| No Model   | 192x128    |       | 200    |
|            | 192x128    |       | None   |
|            |            |       |        |

## Screenshot
![[Pasted image 20230227201936.png]]

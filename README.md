# Face2Led
Face2Led is a Software to convert facial expressions into stylized Images on a Led-Matrix or any other display.

## Used Packages
- **DeepFace** for expression recognition
- **OpenCV** for camera feeds
- **PyGame** for the Software-Matrix
- **lxml** for parsing of the X-SVG
- **numpy** for image and data manipulation 

## How it works
The Software is based on a Pipeline approach. there are multiple stages of the pipeline as outlined bellow whitch kann have multiple Layers itself to create the final output to the LED-Matrix. To Create the final pipeline the Builder pattern is used. you can define the functions used to create/alter the final output. 

## Pipelinedescription
The results of all Pipeline stages are 
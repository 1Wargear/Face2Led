# Face2Led
Face2Led is a Software to convert facial expressions into stylized images on a Led-Matrix or any other display.

## Quick-start
1. Download the repository
2. Install all the dependent Packages as outlined in Used Packages
3. Change the face.xsvg in the asset's folder to your linking
4. start the program.py to show the Software-Led-matrix
5. open localhost:4500 to access the API
6. look into your Web-Cam and have fun

## Used Packages
- **DeepFace** for expression recognition
- **OpenCV** for camera feeds
- **PyGame** for the Software-Matrix
- **lxml** for parsing of the X-SVG
- **numpy** for image and data manipulation 

## How it works
The Software is based on a Pipeline approach. There are multiple stages of the pipeline as outlined below, which can have multiple Layers itself to create the final output to the LED-Matrix. To create the final pipeline, the Builder pattern is used. You can define the functions used to create/alter the final output. 

## Pipeline description
The results of all pipeline stages are accumulated in a dictionary, which is passed down to every pipeline stage as the first parameter. Modifications can be down at any stage, but the effect of the alteration depends on the other functions down stream.

![Pipeline](/docs/Pipeline.drawio.svg)

## API
The API is accessible under [localhost:4500](localhost:4500)
The index page shows Product Name and Product Version

The other Endpoints are listed below:

1. **setExpression**: sets the Face expression to a constant value

    localhost:4500/setExpression/angry

2. **clearExpression**: clears the fixed expression and returns to Face detection

    localhost:4500/clearExpression

## XSVG
To create your own Face, you have to start by creating the SVG File for it. Then just copy it to svg portion of the XSVG-File and start adding Variables.

Variables are in this format: \$NameOfVariable\$
and replace the value at that position. 

Re-add the Value in the default section alongside the Variable name.

Finally create a preset with the expression as its name, and you are good to go.
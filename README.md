I used these files to process my massive 100 million point GeoTiff file into something more manageable.
I reduced the number of points to 10 million and assigned a color to each point based on it's elevation.
Then I used another function to compress the file into a gzip.
Finally I uploaded the file to AWS S3.

Here's the link to the final product: https://block-island.netlify.app/
And the link to the frontend code: https://github.com/katieperry4/block-island-frontend

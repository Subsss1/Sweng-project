mkdir build
cp -f ./Setup.md ./build/Setup.md
cp -f ./Dockerfile-prod ./build/Dockerfile
cp -f ./dissector/ismachine.lua ./build/ismachine.lua
cp -rf ./dissector/server ./build/server
cp -f ./model/dump/RFC_model.pkl ./build/server/model.pkl
zip -r build.zip build
rm -r build
echo "build.zip is created."

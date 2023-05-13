import React, { useState, useEffect } from 'react';
import { View, Image, Text } from 'react-native';
import * as ImageManipulator from 'expo-image-manipulator';

const path = 'C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/my-app/assets/ABRW.jpg';

const App = () => {
  const [image, setImage] = useState(null);
  const [heightPixels, setHeightPixels] = useState(0);
  const [widthPixels, setWidthPixels] = useState(0);

  useEffect(() => {
    (async () => {
      const { uri, width, height } = await ImageManipulator.manipulateAsync(path, [], { format: 'jpg' });
      setImage(uri);
      setHeightPixels(height);
      setWidthPixels(width);
    })();
  }, []);

  return (
    <View>
      {image && <Image source={{ uri: image }} />}
      <Text>{`Height in pixels: ${heightPixels}`}</Text>
      <Text>{`Width in pixels: ${widthPixels}`}</Text>
    </View>
  );
};

export default App;

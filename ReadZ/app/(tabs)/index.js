import React, {FC, useState, useRef} from 'react';

import Constants from 'expo-constants';
import * as Speech from 'expo-speech';

import { HighlightedText } from  'react-native-highlighted-text'
import CircleButton from '@/components/CircleButton';
import Button from '@/components/Button';
import ImageViewer from '@/components/ImageViewer';
import IconButton from '@/components/IconButton';

import Slider from '@react-native-community/slider';

import { View, StyleSheet, Platform, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import * as MediaLibrary from 'expo-media-library';
import { type ImageSource } from "expo-image";
import { captureRef } from 'react-native-view-shot';
import domtoimage from 'dom-to-image';

const PlaceholderImage = require('@/assets/images/0262/5.jpg');

const SpeechTest: FC = () => {
    const [showAppOptions, setShowAppOptions] = useState(true);
    const [currentRate, setcurrentRate] = useState(0.2);
    const [displayText, setDisplayText] = useState('');
    const imageRef = useRef(null);
    const [selectedImage, setSelectedImage] = useState(undefined);



    // const inputValue = 'Hey this is an interesting sentence';

    const pausePlay = () => {
        Speech.pause();
        }
        
    const resumePlay = () => {
        Speech.resume();
        }
        
    const stopPlay = () => {
        Speech.stop();
        }
        
        async function alertIfSpeaking() {
            let speaking = await Speech.isSpeakingAsync();
            if (speaking) {
              alert('speaking')
            } 
          }

    const handlePlay = () => {
        const inputValue = 'In the busy city of Nairobi, far away from a caring life at home, lived a group of homeless boys. They welcomed each day just as it came. On one morning, the boys were packing their mats after sleeping on cold pavements. To chase away the cold they lit a fire with rubbish. Among the group of boys was Magozwe. He was the youngest.';
        setShowAppOptions(false)
        Speech.speak(inputValue, {
            rate:currentRate,
            onPause: () => {alert('paused')},
            onDone: () => {
                setDisplayText(inputValue)
            },
          onBoundary:(boundaries) => {
              const {charIndex, charLength} = boundaries;
              const word = inputValue.substring(charIndex, charIndex+charLength)
              console.log(boundaries, word)

            //   const cleanSentence = inputValue.replace('[[','')
            //   cleanSentence = cleanSentence.replace(']]','')

              const finalIndex = charIndex + charLength
              FinalSentence = [inputValue.slice(0, charIndex),'[[' + word + ']]', inputValue.slice(finalIndex)].join('');

              setDisplayText(FinalSentence)
          }
        });
    }
    return (
        
        <View style={styles.container}>
            {/* <Button title={'play'} onPress={handlePlay}/> */}
            {/* <Button title={'Check'} onPress={alertIfSpeaking}/> */}

            <View style={styles.imageContainer}>
                <View ref={imageRef} collapsable={false}>
                <ImageViewer imgSource={PlaceholderImage} selectedImage={selectedImage} />
                </View>
            </View>
        <View>
        </View>
  


        {showAppOptions ? (
        <View style={styles.optionsContainer}>
        

            <Text style={styles.paragraph}>
            Speed: {currentRate.toFixed(1)}
            </Text>
          <Slider
            style={styles.slider}
            minimumValue={0.1}
            maximumValue={1}
            value={currentRate}
            onSlidingComplete={setcurrentRate}
          />
                    <Button theme="primary" label="Start" onPress={handlePlay} />
        </View>
      ) : (
        <View style={styles.footerContainer}>
       
            <HighlightedText
            style={styles.paragraph}
            highlightedTextStyles={[
                {
                fontSize:  18,
                fontWeight:  'bold',
                color: 'salmon'
                }
            ]}
            >
            {displayText}
            </HighlightedText>

            <View style={styles.optionsRow}>
              <IconButton icon="refresh" label="Reset" onPress={alertIfSpeaking} />
              <CircleButton onPress={alertIfSpeaking} />
              <IconButton icon="save-alt" label="Save" onPress={alertIfSpeaking} />
            </View>

          {/* <Button label="Speak!" onPress={() => Speech.speak('Hello World!')} /> */}
          {/* <Button theme="primary" label="Choose a photo" onPress={pickImageAsync} /> */}
          {/* <Button label="Use this photo" onPress={() => setShowAppOptions(true)} /> */}
        </View>
        
      )}
        </View>

        
    );
};

export default SpeechTest;



const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#25292e',
        alignItems: 'center',
      },
      imageContainer: {
      },
      footerContainer: {
        top:5,
        padding:20,
        alignItems: 'center',
      },
      optionsContainer: {
        position: 'absolute',
        bottom: 20,
      },
      optionsRow: {
        top:10,
        alignItems: 'center',
        flexDirection: 'row',
      },
      text: {
        padding:10,
        color: '#fff',
      },
    paragraph: {
        margin: 2,
        fontSize: 18,
        textAlign: 'center',
        color: '#fff'
    },
    slider: {
        width: '90%',
         height: 40,
      },
});

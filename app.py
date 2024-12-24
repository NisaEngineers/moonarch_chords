import streamlit as st
import autochord
import pretty_midi
import librosa
from moonarch import MusicToChordsConverter
import time

# Set the title of the app
st.title('Chord Finder')

# Upload audio file
audio_file = st.file_uploader("Upload a song", type=["mp3", "wav"])

if audio_file is not None:
    st.write("File uploaded successfully.")
    
    # Placeholder for progress bar
    progress_bar = st.progress(0)
    
    # Simulate file processing
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    st.write("File processing complete.")

    if st.button('Find Chords'):
        with st.spinner('Extracting chords and generating MIDI...'):
            # Convert the uploaded file to a file path
            audio_file_path = f'/tmp/{audio_file.name}'
            with open(audio_file_path, 'wb') as f:
                f.write(audio_file.getbuffer())

            # Convert music to chords and save as MIDI
            output_midi_file = 'Sample_Piano_Chords.mid'
            converter = MusicToChordsConverter(audio_file_path)
            converter.recognize_chords()
            converter.generate_midi()
            converter.save_midi(output_midi_file)

            st.success('Chords extraction and MIDI generation complete!')

            if st.button('Download MIDI file'):
                with open(output_midi_file, 'rb') as f:
                    st.download_button(
                        label="Download MIDI file",
                        data=f,
                        file_name=output_midi_file,
                        mime='audio/midi'
                    )

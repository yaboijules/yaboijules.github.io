import synthesizer
player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

input()

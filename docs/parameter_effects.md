# Parameter Effects in Story Generation

This document analyzes how different generation parameters affect the output of the AI story generation system.

The system uses Ollama to generate text and supports parameters such as Temperature, Top P, and Repeat Penalty.

---

## Temperature

Temperature controls the randomness of the generated text.

Lower values make the output more deterministic and predictable, while higher values make the output more creative and diverse.

### Example Prompt

Describe a sunset over the mountains.

### Temperature = 0.01 (Low)

Output:

The sun slowly sets behind the mountains. The sky turns orange and red as the light fades. The scene is calm and quiet.

### Temperature = 1.5 (High)

Output:

The blazing sun melts into the jagged peaks, scattering rivers of crimson and gold across the sky. Shadows dance across the mountain ridges as the world slips into twilight.

Observation:

Low temperature produces predictable and safe text. High temperature produces creative and descriptive text.

---

## Top P

Top P (nucleus sampling) controls how many possible tokens the model considers while generating text.

Lower values restrict the model to more probable words, while higher values allow more diverse choices.

### Example Prompt

A dragon appears in the sky.

### Top P = 0.3

Output:

A dragon appears in the sky. People look up in fear as the large creature flies above the city.

### Top P = 0.95

Output:

A massive dragon bursts through the clouds, its wings casting enormous shadows across the land as flames shimmer in its glowing eyes.

Observation:

Lower Top P creates more conservative text. Higher Top P allows more varied and imaginative responses.

---

## Repeat Penalty

Repeat penalty reduces repetition in generated text.

Higher values discourage the model from repeating the same words or phrases.

### Example Prompt

The knight walked through the dark forest.

### Repeat Penalty = 1.0

Output:

The knight walked through the dark forest. The dark forest was quiet and the knight walked slowly through the forest.

### Repeat Penalty = 1.3

Output:

The knight stepped carefully beneath the ancient trees, listening to the whisper of leaves and distant owls.

Observation:

Higher repeat penalty reduces repetitive text and improves narrative flow.
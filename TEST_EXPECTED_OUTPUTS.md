# SoulVerse Expected Outputs

## General expectations

- The app should use one of the SoulVerse tools instead of citing Bible text from memory.
- The response should include an exact Bible verse text returned from the API when the lookup succeeds.
- The widget should display a clear heading, the verse text, the reference, and a brief reflection.
- The tone should be gentle, supportive, and non-judgmental.

## Specific expectations

### Anxiety prompt

- should trigger `get_comfort_verse`
- should return a card for anxiety or peace
- should include a real Bible reference such as `Filipenses 4:6-7`

### Loneliness prompt

- should trigger `get_comfort_verse`
- should return a card with a theme matching loneliness, companionship, courage, or divine presence

### Explicit reference prompt

- should trigger `get_bible_verse`
- should return the exact requested reference when available
- should not reinterpret the request as a general emotional lookup

### Guilt prompt

- should trigger `get_comfort_verse`
- should use language of forgiveness, restoration, or confession without accusation

### Exhaustion prompt

- should trigger `get_comfort_verse`
- should return a verse about rest or relief from burden

### Invalid reference prompt

- should trigger `get_bible_verse`
- should return an error-style response or card
- should not hallucinate verse text for an invalid reference

const createMovie = (scene, characters, effects) => {
  // Create a new movie using the provided scene, characters, and effects
  const movie = new Movie(scene);

  // Add characters to the movie
  characters.forEach((character) => {
    movie.addCharacter(character);
  });

  // Apply effects to the movie
  effects.forEach((effect) => {
    movie.applyEffect(effect);
  });

  return movie;
};

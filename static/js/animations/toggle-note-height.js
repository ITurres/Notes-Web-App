const noteTextarea = document.querySelectorAll("[data-note-textarea]");

noteTextarea.forEach((note) => {
  note.addEventListener("click", () => {
    note.classList.toggle("large");
    note.nextElementSibling.nextElementSibling.classList.toggle("hidden");
  });
});

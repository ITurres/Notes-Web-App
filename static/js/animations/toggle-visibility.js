const newNoteForm = document.querySelector("[data-new-note-form]");
const toggleNewNoteFormBtn = document.querySelectorAll(
  "[data-toggle-new-note-form]"
);

const toggleHiddenClass = (elements, element) => {
  elements.forEach((el) => {
    el.classList.toggle("hidden");
  });
  element.classList.toggle("hidden");
};

toggleNewNoteFormBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    toggleHiddenClass(toggleNewNoteFormBtn, newNoteForm);
  });
});

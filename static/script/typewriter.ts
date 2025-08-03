const typingSpeed = 5; // ms per character

// Sleep function
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

// Main recursive work function
const typewrite = async (parent: Element | null, element: Element | null) => {
  if (element == null) {
    return;
  }

  const tag = element.tagName;
  const emptyElement = document.createElement(tag);

  if (parent == null) {
    console.log("TYPEWRITER: root element of type %s", tag);

    element.replaceWith(emptyElement);
    const children = Array.from(element.children);
    for (let i = 0; i < children.length; i++) {
      await typewrite(emptyElement, children[i]);
    }
  } else if (element.children.length == 0) {
    if (element.textContent == null) {
      console.log("TYPEWRITER: appending non-typed element of type %s", tag);

      parent.appendChild(element);
      return;
    }

    console.log(
      "TYPEWRITE: typing element of type %s with text '%s'",
      tag,
      element.textContent,
    );

    parent.appendChild(emptyElement);
    emptyElement.textContent = "";
    for (let i = 0; i < element.textContent.length; i++) {
      emptyElement.textContent += element.textContent[i];
      await sleep(typingSpeed);
    }
  } else {
    console.log("TYPEWRITE: traversing nested element of type %s", tag);

    parent.append(emptyElement);
    const children = Array.from(element.children);
    for (let i = 0; i < children.length; i++) {
      await typewrite(emptyElement, children[i]);
    }
  }
};

document.addEventListener("DOMContentLoaded", async function () {
  const container = document.querySelector(".typewriter");
  await typewrite(null, container);
});

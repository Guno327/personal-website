let keyPressedSinceLoad = false;
// Listen for the first keydown event
document.addEventListener("keydown", function onKeydown() {
  keyPressedSinceLoad = true;

  // Optional: Remove the listener after first keypress to save resources
  document.removeEventListener("keydown", onKeydown);
});

function typeElement(
  source: HTMLElement,
  target: HTMLElement,
  delay: number,
): void {
  const cloneAndType = async (
    srcNode: Node,
    parent: HTMLElement,
  ): Promise<void> => {
    if (srcNode.nodeType === Node.TEXT_NODE) {
      const text = (srcNode as Text).textContent || "";
      for (let char of text) {
        if (keyPressedSinceLoad) {
          return;
        }

        parent.appendChild(document.createTextNode(char));
        await new Promise((resolve) => setTimeout(resolve, delay));
      }
    } else if (srcNode.nodeType === Node.ELEMENT_NODE) {
      const srcElem = srcNode as HTMLElement;
      const newElem = document.createElement(srcElem.tagName.toLowerCase());

      // Copy all attributes
      for (let attr of Array.from(srcElem.attributes)) {
        newElem.setAttribute(attr.name, attr.value);
      }

      parent.appendChild(newElem);

      // Recursively type each child node
      for (let child of Array.from(srcElem.childNodes)) {
        await cloneAndType(child, newElem);
      }
    }
  };

  // Clear the target element before starting
  target.innerHTML = "";

  // Start async typing
  (async () => {
    for (let child of Array.from(source.childNodes)) {
      if (keyPressedSinceLoad) {
        source.style.visibility = "visible";
        target.replaceWith(source);
        return;
      }

      await cloneAndType(child, target);
    }
  })();
}

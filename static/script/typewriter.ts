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
      await cloneAndType(child, target);
    }
  })();
}

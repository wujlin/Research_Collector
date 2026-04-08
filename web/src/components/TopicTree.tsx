"use client";

import type { Topic } from "../lib/generated";

type TopicTreeProps = {
  topics: Topic[];
};

export function TopicTree({ topics }: TopicTreeProps) {
  const roots = topics
    .filter((topic) => !topic.parent_key)
    .sort((left, right) => left.key.localeCompare(right.key));
  const childrenByParent = new Map<string, Topic[]>();

  topics.forEach((topic) => {
    if (!topic.parent_key) {
      return;
    }
    const siblings = childrenByParent.get(topic.parent_key) ?? [];
    siblings.push(topic);
    childrenByParent.set(topic.parent_key, siblings);
  });

  childrenByParent.forEach((children) => {
    children.sort((left, right) => left.key.localeCompare(right.key));
  });

  return (
    <div className="topicTree">
      {roots.map((root) => (
        <section className="card" key={root.key}>
          <p className="eyebrow">Layer {root.depth + 1}</p>
          <h3>{root.display_name}</h3>
          <p className="muted">{root.description || root.key}</p>
          <ul className="topicTreeList">
            <TopicBranch topic={root} childrenByParent={childrenByParent} />
          </ul>
        </section>
      ))}
    </div>
  );
}

type TopicBranchProps = {
  topic: Topic;
  childrenByParent: Map<string, Topic[]>;
};

function TopicBranch({ topic, childrenByParent }: TopicBranchProps) {
  const children = childrenByParent.get(topic.key) ?? [];

  return (
    <li>
      <div className="topicTreeNode">
        <div>
          <strong>{topic.display_name}</strong>
          <div className="topicKey">{topic.lineage.join(" / ")}</div>
          {topic.description ? <p className="muted">{topic.description}</p> : null}
        </div>
        <div className="topicTreeMeta">
          <span className="pill">{topic.paper_count} papers</span>
          <span className="pill">{topic.is_leaf ? "leaf" : `branch · L${topic.depth + 1}`}</span>
        </div>
      </div>
      {children.length ? (
        <ul className="topicTreeList topicTreeNested">
          {children.map((child) => (
            <TopicBranch key={child.key} topic={child} childrenByParent={childrenByParent} />
          ))}
        </ul>
      ) : null}
    </li>
  );
}

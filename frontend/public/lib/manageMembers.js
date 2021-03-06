export function getAllChangedMembers(oldMembers, newMembers, members_prop_name) {
  const oldCreatorId = oldMembers.filter((m) => m.role.name === "Creator")[0].id;
  const newCreatorId = newMembers.filter((m) => m.role.name === "Creator")[0].id;
  const deletedMembers = oldMembers.filter((m) => !newMembers.find((cm) => cm.id === m.id));
  const creatorChange =
    oldCreatorId != newCreatorId ? newMembers.filter((cm) => cm.id === newCreatorId) : [];
  const createdMembers = newMembers.filter(
    (cm) =>
      !oldMembers.find((m) => m.id === cm.id) &&
      !creatorChange.find((m) => m.id === cm.id) &&
      !(oldCreatorId != newCreatorId && cm.id === oldCreatorId)
  );
  const updatedMembers = newMembers.filter(
    (cm) =>
      !oldMembers.includes(cm) &&
      !createdMembers.includes(cm) &&
      !creatorChange.find((m) => m.id === cm.id) &&
      !(oldCreatorId != newCreatorId && cm.id === oldCreatorId)
  );
  const allChangedMembers = [
    ...deletedMembers.map((m) => ({ ...m, operation: "delete" })),
    ...updatedMembers.map((m) => ({ ...m, operation: "update" })),
  ];
  if (createdMembers.length > 0)
    allChangedMembers.push({ [members_prop_name]: [...createdMembers], operation: "create" });

  if (creatorChange.length > 0)
    allChangedMembers.push({ new_creator: creatorChange[0], operation: "creator_change" });

  return allChangedMembers;
}
